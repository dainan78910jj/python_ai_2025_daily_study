Lab 20250902 - 20250905: Santa, not santa
 
Summer is over and winter is soon coming. And every year i always miss seeing santa clause on the 24:th of december. I havent seen him for years. And im starting to miss santa clause. 
 
This year i decided to set up an object detection camera im my house. So whenever santa clause comes creeping in to my house the alarm should go of and my camera should say "Found santa"!
 
so what you guys need to do is to create an object detection on santa and not santa. See picture:
 
So in other words you guys need a model that can detect santa in a picture. And if it dosent then it should say "not santa". You can work in a group 2-3 people if you want. Up to you. 
 
 
Feel free to ask chatgpt how you would solve my problem so i dont miss santa this year too. 
 
Here is a good start on how you could solve my issue with santa:
 
## Dataset

## A) Collect images

 - Positive class (Santa): Santa photos in diverse poses, outfits, lighting, partial occlusions, and backgrounds (indoor/outdoor).
 - Negative class (no labels): “hard negatives”—winter scenes, red clothing, crowds, Christmas trees, gifts, reindeer, no Santa.
 - Aim for ~500–1500 images total to start (at least 200 with Santa). More is better.

## B) Annotate (bounding boxes)

 - Use a tool like LabelImg, MakeSense.ai, or Label Studio.
 - Draw boxes only around visible Santas (full or partial; exclude posters/toys unless you want the model to trigger on them).
 - Class list: santa only.
 - Keep consistent: include hat/beard/coat in the box when possible.

## C) Split

 - Train 70% / Val 15% / Test 15%
 - Ensure no near-duplicates across splits (same photo burst should stay in one split).
 - Keep negatives in all splits. Negatives are images with no Santa → they have no boxes.

## D) Augmentation plan (train only)

 - Horizontal flip (ON).
 - Small rotations (±10°), slight scale/zoom.
 - Mild brightness/contrast jitter.
 - Avoid vertical flips (upside-down Santa) unless you really want that.