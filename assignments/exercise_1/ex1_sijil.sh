#! /bin/bash


# storing the path of the directory containing the exercises
working_dir=/home/sijil/SISSA/python_crash_course_assignments/assignments/ex1 
cd $working_dir


# TASK1 : creating a copy of the directory "bandpasses"
[ ! -d bandpass_sijil ] && cp -r bandpass_raw bandpass_sijil

cd bandpass_sijil
# TASK2 : counting the occurences of each extentions

# Create an empty array to store extensions
extensions=()
for FILE in *;do

   # Extraxct the extension 
   extension="${FILE##*.}"

   # IF extention is not in the array, add it    
   if [[ ! " ${extensions[@]} " =~ " $extension " ]]; then
        extensions+=("$extension")
    fi
done

# Print the types and counts
for ext in "${extensions[@]}"; do
    count=$(find "$working_dir/bandpass_sijil" -maxdepth 1 -type f -name "*.$ext" | wc -l)
    echo "$ext: $count"
done


# TASK3 : renaming the files based on the presence of the "photons" or "energy" in the comments and sstoring the the file_names which doesn't contain either of these two comments


for FILE in *;do

   #Extractig the second line of the file using a combination of head and tail and storing the string in the variable second_line
    second_line=$(head -n 2 "$FILE" | tail -1);
    filename="${FILE%.*}"  #extracting the file name without the extention (parameter expansion)
		


    # Check for cases
    case "$second_line" in
        *"photon"*)
            # Move the file to the new name "photons.filt"
	    mv "$FILE" "$filename.photons.filt";;
        *"energy"*)
            # Move the file to the new extension "energy.filt"
            mv "$FILE" "$filename.energy.filt";;
        *)
            echo "Skipped $filename, no 'photon' or 'energy' in the second line";;
    esac

done

cd $working_dir

