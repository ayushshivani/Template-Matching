import sys
import numpy as np
import cv2
import os

input_arr = sys.argv
slides_img = []
slides_name = []
ans = [] 


def load_img_from_folder(folder):
	images = []
	for image in os.listdir(folder):
		img_rgb = cv2.imread(os.path.join(folder,image))
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
		# print(os.path.join(folder,image))
		if img_gray is not None:
			images.append(img_gray)
			slides_name.append(image)
			# cv2.imshow('image',img)
			# cv2.waitKey(1000)
	return images


def cv2_template_matching(template,frame):
	# type(frame)
	frame.astype(np.float32)
	template.astype(np.float32)

	res = cv2.matchTemplate(frame,template,cv2.TM_CCOEFF_NORMED) 
	# res = cv2.matchTemplate(frame,template,cv2.TM_CCOEFF_NORMED)
	return res


if __name__ == "__main__":

	slides_img = load_img_from_folder(sys.argv[1])

	for image in os.listdir(input_arr[2]):
		img_rgb = cv2.imread(os.path.join(input_arr[2],image))
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
		res = []
		max_perc = 0
		for index in range(len(slides_img)):
			# print(slide)
			match_perc = cv2_template_matching(slides_img[index],img_gray)
			res.append(match_perc[0])
			if match_perc > max_perc:
				max_perc = match_perc
				slide_ans = slides_name[index]
		
		print(image,slide_ans)










