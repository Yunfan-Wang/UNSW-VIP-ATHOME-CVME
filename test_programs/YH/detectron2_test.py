from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2 import model_zoo

import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("model", type=str)
parser.add_argument("input", type=str)
parser.add_argument('-v', '--video', action='store_true')
args = parser.parse_args()


class Detector:    
    def __init__(self, model_type):
        self.cfg = get_cfg()
        self.model_type = model_type
        
        config_file = ""

        # object detection
        if model_type == "OD":
            config_file = "COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml"
        # instance segmentation
        elif model_type == "IS":
            config_file = "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
        # keypoint detection
        elif model_type == "KP":
            config_file = "COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml"
        # panoptic segmentation
        elif model_type == "PS":
            config_file = "COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml"
        # LVIS segmentation
        elif model_type == "LVIS":
            config_file = "LVISv0.5-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml"
        
        self.cfg.merge_from_file(model_zoo.get_config_file(config_file))
        self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(config_file)
        
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7
        self.cfg.MODEL.DEVICE = "cpu"
        
        self.predictor = DefaultPredictor(self.cfg)
    
    def run_image(self, image_path):
        image = cv.imread(image_path)
        output = self.predict(image)
        cv.imshow("Result", output.get_image()[:, :, ::-1])
        cv.waitKey(0)
    
    def run_video(self, video_path):
        video = cv.VideoCapture(video_path)
        (success, image) = video.read()
        
        while success:
            output = self.predict(image)
            cv.imshow("Result", output.get_image()[:, :, ::-1])
            key = cv.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            (success, image) = video.read()
    
    def predict(self, image):
        if self.model_type == "PS":
            predictions, segment_info = self.predictor(image)["panoptic_seg"]
            visualizer = Visualizer(image[:, :, ::-1], metadata=MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]))
            output = visualizer.draw_panoptic_seg_predictions(predictions.to("cpu"), segment_info)
        else:
            predictions = self.predictor(image)
            visualizer = Visualizer(image[:, :, ::-1], metadata=MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), instance_mode=ColorMode.IMAGE)
            output = visualizer.draw_instance_predictions(predictions["instances"].to("cpu"))
        return output    


if __name__ == "__main__":
    model = args.model
    input = args.input
    
    detector = Detector(model)
    
    if args.video:
        detector.run_video(input)
    else:
        detector.run_image(input)
