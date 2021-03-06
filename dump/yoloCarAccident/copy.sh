## declare an array variable
rm -r frames
mkdir frames

arr=(598 743 1039 1205 1473 1577 1863)
## now loop through the above array
for i in "${arr[@]}"
do
   # echo "frame_0000$i.jpg"
   # results

   mkdir frames/$i

   for (( j=1; j<=80; j++ ))
   do
   	
   	let k=$i-40+$j
   	cp results/frame_00000$k.jpg frames/$i/frame_00000$k.jpg
   	cp results/frame_0000$k.jpg frames/$i/frame_0000$k.jpg
   	cp results/frame_000$k.jpg frames/$i/frame_000$k.jpg
   	cp results/frame_00$k.jpg frames/$i/frame_00$k.jpg
   
   done

   # or do whatever with individual element of the array
done