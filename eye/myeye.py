# just main for eye
# in: jpg
# out: matrix of a board state
import cv2
import numpy as np


def see():
	img = cv2.imread('data/try0.png')
	# print(img)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cor = cv2.findChessboardCorners(gray, (7, 9))
	print(cor)
	return [[], []]


def get_input():
	return input("Your move: ")


'''
https://blog.csdn.net/u010128736/article/details/52875137
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html
'''


def demo():
	# termination criteria
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
	
	# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
	objp = np.zeros((6 * 7, 3), np.float32)
	objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
	
	# Arrays to store object points and image points from all the images.
	objpoints = []  # 3d point in real world space
	imgpoints = []  # 2d points in image plane.
	
	img = cv2.imread('data/try2.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	# Find the chess board corners
	ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
	print(ret)
	
	# If found, add object points, image points (after refining them)
	if ret == True:
		objpoints.append(objp)
		
		corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
		imgpoints.append(corners2)
		
		# Draw and display the corners
		img = cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
		cv2.imshow('img', img)
		cv2.waitKey(5000)
	
	cv2.destroyAllWindows()


if __name__ == '__main__':
	demo()