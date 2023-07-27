# import all necessary packages
import cv2
import numpy as np

# import object_detection module- it contains the location of 8*8 grid and location of each chess pieces
import object_detection as od

# image path
path = 'D:/temp/Chess/Chess1.png'


def main():
    # initialise the chess_detection class from the object_detection
    chess =  od.chess_detection()

    # Load the image
    image = cv2.imread(path)

    # get_location method will find the location of 8*8 grid of chess board
    locations = chess.get_location(image)

    # Display the image
    cv2.imshow("Image", image)
     
    # Wait for the user t# Load the imageo press a key
    cv2.waitKey(0)
     
    # Close all windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
