## declare an array variable
arr=(257 338 547 1658 1962 2699 2900 3041 3407 3601 4841 5187 5353 5396 5841 5956 6120 6467 6618 7334 8462 8507 8745 8799 8930 8974 9149 9365 9644 11455 12117 12904 13095 13213 13307 13478 14104 14382 14685 14735 15115 15496 18339 18405 18477 19506 20449 20627 21535 22603)


## now loop through the above array
for i in "${arr[@]}"
do
   # echo "frame_0000$i.jpg"
   # /media/ayush/762271BE227183C1/Ubuntu/ITRI/results
   cp /media/ayush/762271BE227183C1/Ubuntu/ITRI/results/frame_0000$i.jpg frames/frame_0000$i.jpg
   # or do whatever with individual element of the array
done