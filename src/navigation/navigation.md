## Navigation 

This folder contains 5 Jupyter notebooks that navigates the jetbot using computer vision:

1. `road_data_collection.ipynb`: collecting data to train a road following model.
2. `road_train_model.ipynb`: training a road following model.
3. `waypoint_data_collection.ipynb`: collecting data to train a waypoint detection model.
4. `waypoint_train_model.ipynb`: training a waypoint detection model.
5. `navigate.ipynb`: using the road following model and waypoint detection model to navigate the jetbot.

An example setup might look like this:
![Alt text](setup.jpg)
where white masking tape represents roads and red dots represent waypoints.

The models produced are:
- `best_waypoint_model.pth` is an AlexNet model trained on a dataset consisting of 2 classes (each with ~50 images, over 30 epochs) using `waypoint_train_model.ipynb`.
- `best_steering_model_xy.pth` is a ResNet18 model trained on a dataset consisting of images and their associated x,y coordinates indicating the desire direction of motion (~80 images, over 70 epochs) using `road_train_model.ipynb`.
