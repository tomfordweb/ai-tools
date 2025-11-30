import sys
from imutils.perspective import four_point_transform
from pdf2image import convert_from_path
import numpy as np
import pytesseract
import argparse
import imutils
import cv2
import re

pricePattern = r"([0-9]+\.[0-9]+)"
upcPattern = r"([0-9]{4})"

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input receipt image")
ap.add_argument(
    "-d",
    "--debug",
    type=int,
    default=-1,
    help="whether or not we are visualizing each step of the pipeline",
)
args = vars(ap.parse_args())


# Convert PDF pages to PIL Images
# dpi can be adjusted for higher or lower resolution
pages = convert_from_path(args["image"], dpi=200)

pil_image = pages[0]

opencv_image = np.array(pil_image)

# Convert RGB to BGR as OpenCV uses BGR by default
receipt = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

# rotate the image 90* and use psm5 to read the text top down
# (helps in preserving columns)
receipt = cv2.rotate(receipt, cv2.ROTATE_90_CLOCKWISE)

if args["debug"] > 0:
    cv2.imshow("receipt", receipt)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()

text = pytesseract.image_to_string(
    cv2.cvtColor(receipt, cv2.COLOR_BGR2RGB),
    config="--psm 5",
)


if args["debug"] > 0:
    # show the raw output of the OCR process
    print("[INFO] raw output:")
    print("==================")
    print(text)
    print("\n")


# I'm just a midwest meijers man
def processMeijerLineItems(data: list):
    output = list()

    for index, row in enumerate(data):
        if (
            re.search(upcPattern, row) is not None
            and re.search(pricePattern, row) is not None
        ):
            output.append(row)

    return output


processedMeijerItems = processMeijerLineItems(text.split("\n"))

print("[INFO] Formatted output")
print("========================")
for line in processedMeijerItems:
    print(line)
