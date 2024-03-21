#!/bin/bash

for y in {2019..2024}
do
       for m in {01..12}
       do
	       for t in {0..4}
	       do
		       if [ ! -f "$y.$m.$t.json" ]; then
			       echo '' > "$y.$m.$t.json"
		       fi
	       done
       done
done

# borramos los que no son necesarios a hoy: 2024/03
for i in {01..07}
do
	for j in {0..4}
	do
		rm "2019.$i.$j.json"
	done
done

for i in {04..12}
do
	for j in {0..4}
	do
		rm "2024.$i.$j.json"
	done
done
