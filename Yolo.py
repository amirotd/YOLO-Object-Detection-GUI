import numpy as np
import cv2
import os


class Yolo:
    def __init__(self, img, path, conf=0.5, thresh=0.3):
        self.conf = conf
        self.thresh = thresh
        self.img = img
        self.path = path

        self.LabelsPath = os.path.sep.join([self.path, "coco.names"])
        self.WeightsPath = os.path.sep.join([self.path, "yolov3.weights"])
        self.ConfigPath = os.path.sep.join([self.path, "yolov3.cfg"])

        self.LABELS = open(self.LabelsPath).read().strip().split("\n")
        self.boxes = []
        self.confidences = []
        self.classIDs = []

        np.random.seed(42)
        self.COLORS = np.random.randint(0, 255, size=(len(self.LABELS), 3), dtype="uint8")

    def start_process(self):
        net = cv2.dnn.readNetFromDarknet(self.ConfigPath, self.WeightsPath)

        image = cv2.imread(self.img)
        (H, W) = image.shape[:2]

        ln = net.getLayerNames()
        ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

        blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)

        layer_outputs = net.forward(ln)

        for output in layer_outputs:
            for detection in output:

                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                if confidence > self.conf:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    self.boxes.append([x, y, int(width), int(height)])
                    self.confidences.append(float(confidence))
                    self.classIDs.append(classID)

        idxs = cv2.dnn.NMSBoxes(self.boxes, self.confidences, self.conf, self.thresh)

        if len(idxs) > 0:

            for i in idxs.flatten():
                (x, y) = (self.boxes[i][0], self.boxes[i][1])
                (w, h) = (self.boxes[i][2], self.boxes[i][3])

                color = [int(c) for c in self.COLORS[self.classIDs[i]]]
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                text = "{}: {:.4f}".format(self.LABELS[self.classIDs[i]], self.confidences[i])
                cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        while True:
            cv2.imshow("Image", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = Yolo('dog.jpg')
    app.start_process()
