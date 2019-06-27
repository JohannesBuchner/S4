echo "generating ... ====="

for i in 1 2 3 4; do 
	for j in 1 2 3 4 5; do 
		python3 mygen.py $i $j
	done
done

echo "generating done ====="
python3 myavg_parallel.py output_?_?.txt




