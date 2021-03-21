# Matrix-Image-Reader
An app that takes in a hand-drawn matrix and converts it into an Matrix object that can be used in future calculations. Built for HackPSU!

## Goal
1. Read in any hand-drawn matrix and convert to a Sympy Matrix object
2. Scale only to single digits and positive numbers
3. Be able to apply matrix operations, like RREF, determinant, eigenvectors, and more!
4. Demo with website, being able to take in images of hand-drawn matrices

## Inspiration
I wanted to step into the world of machine learning and computer vision and create an app that would be useful for me and hopefully other students. I figured that most people hated checking their Linear Algebra homework since typing in a 4x4 matrix is typing 16 elements. So I thought, _" Just take a picture of your matrix, supply the dimension, and you're home free! "_

## What it does
M.I.R helps you quickly create matrix objects with an image of one. Just scan a quick image and run it through the code, and you can quickly apply operations, like dot and cross product, RREF, finding determinant or eigenvectors, and more!

## How we built it
I built the app mainly with TensorFlow. NumPy, OpenCV, and Sympy. I used the MNIST dataset for hand-drawn digits to create the model to recognize 28x28 images. Then created an algorithm to create contours around each digit in the matrix and apply it to predict each number. Once the numbers are predicted, the user can use Sympy's Matrix operations to check the answers to their homework.

## Challenges we ran into
Since it was my first time working by myself in a Hackathon, the workload was a lot. I'm also very green in computer vision and machine learning, so the concepts were challenging (but fun!). The issues were Tensorflow not being compatible with the Mac Mini, so I had to use Google Colab, also trying to resize my hand-drawn images so that the model would work was also challenging since the aspect ratio changes, i.e., a 1 looked like a 9 or vice versa.  

## Accomplishments that we're proud of
I am proud that I got the app to work most of the time and really happy I got my feet wet with this first project!

## What we learned
I learned a lot of computer vision techniques, like converting an image to gray-scale, blurring, and finding contours. Then filtering contours and drawing shapes on images. Also found out a lot about the requirements to make a model work with your own hand-drawn digits, like converting them to 28x28 pixels and giving each digit a border. 

## What's next for Matrix Image Reader
I'm hoping to make the M.I.R. a desktop app using DearPyGui, so the user can just select any number of matrices from their folder and click buttons for whatever operations they wish to apply. I'm also hoping to improve the accuracy of the model since there are some weird inaccuracies. 
