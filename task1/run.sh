#! /bin/bash

while [ $# != 0 ]
  do
    if [ $1 == "--input_folder" ]
      then
        input_folder=$2;
    fi
    if [ $1 == "--extension" ]
      then
        extension=$2;
    fi
    if [ $1 == "--backup_folder" ]
      then
        backup_folder=$2;
    fi
    if [ $1 == "--backup_archive_name" ]
      then
        backup_archive_name=$2;
    fi
    shift 2
  done

mkdir "$backup_folder"

for val in $(find $input_folder -type f -name "*.$extension")
  do
    cp --backup=numbered "$val" "$backup_folder/"
  done

tar -czf "$backup_archive_name" "$backup_folder"

echo "done"

