"""
My code was written based on the given references for finding dominant colors
https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

No additional features were added
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def find_histogram(clt):
    num_labels = np.arange(0, len(np.unique(clt.labels_))+1)
    (hist, _) = np.histogram(clt.labels_, bins=num_labels)
    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # RGB
    frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Draw region of interest
    cv2.rectangle(frame,(900,450),(1050,550),(255,0,0),5)
    sub_frame = frame[450:500, 950:1000]

    # Reshape sub frame for Kmeans
    sub_frame = sub_frame.reshape((sub_frame.shape[0] * sub_frame.shape[1], 3))
    clt = KMeans(n_clusters = 3)
    clt.fit(sub_frame)

    # Find dominant color
    hist = find_histogram(clt)
    dominant_color = max(zip(hist, clt.cluster_centers_), key=lambda item: item[0])[1]
    
    # Display dominant color in top left
    cv2.rectangle(frame,(50,50),(200,200),dominant_color,-1)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()