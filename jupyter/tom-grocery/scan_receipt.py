from pdf2image import convert_from_path
import numpy as np
import pytesseract
import argparse
import cv2
import re
import os





# I'm just a midwest meijers man
def processMeijerLineItems(data: list):
    output = list()

    pricePattern = r"([0-9]+\.[0-9]+)"
    upcPattern = r"([0-9]{4})"
    for index, row in enumerate(data):
        if (
            re.search(upcPattern, row) is not None
            and re.search(pricePattern, row) is not None
            and "was" not in row
            and "DEPOSIT" not in row
        ):
            # Remove everything after the product name (keep UPC and Product only)
            output.append(re.sub(pricePattern + r"\s+.*", "", row))

    return output


def convertPdfToImage(path: str):
    pages = convert_from_path(path, dpi=200)

    pil_image = pages[0]

    opencv_image = np.array(pil_image)

    # Convert RGB to BGR as OpenCV uses BGR by default
    image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

    # rotate the image 90* and use psm5 to read the text top down
    # (helps in preserving columns)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    return image


def extractReceipt(args, path: str):
    receipt = convertPdfToImage(path)
    if "debug" in args:
        cv2.imshow("receipt", receipt)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()

        # PSM 5 flips it on its side so we parse everything as columns based on their vertical orientation
        # it is slightly more accurate.
    text = pytesseract.image_to_string(
        cv2.cvtColor(receipt, cv2.COLOR_BGR2RGB),
        config="--psm 5",
    )

    if "debug" in args:
        # show the raw output of the OCR process
        print("[INFO] raw output:")
        print("==================")
        print(text)
        print("\n")

    processedData = processMeijerLineItems(text.split("\n"))

    if "debug" in args:
        print("[INFO] Formatted output")
        print("========================")
        for line in processedData:
            print(line)
    return processedData


def scan(args):
    items = list()

    
    if args["directory"]:
        for item_name in os.listdir(args["directory"]):
            full_path = os.path.join(args["directory"], item_name)
            if os.path.isfile(full_path):
                items = items + extractReceipt(args, full_path)
        pass

    elif args["image"]:
        items = extractReceipt(args, args["image"])
    else:
        raise RuntimeError('unable to process argument')
    for item in items:
        print(item)
    return items

