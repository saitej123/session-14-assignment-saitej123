
### Developed by Sai Teja Macharla 
#### *Email: macharlasaiteja@gmail.com*  
<br>

#### No Test cases provided for this Assignment.
<br>

#  Session 14 - Context Managers
## Topics Covered 
- Decimal Precision
- Generators and Context Manager


## **Project: Description** 

For this project you have 4 files containing information about persons.

The files are:

personal_info.csv - personal information such as name, gender, etc. (one row per person)
vehicles.csv - what vehicle people own (one row per person)
employment.csv - where a person is employed (one row per person)
update_status.csv - when the person's data was created and last updated
Each file contains a key, SSN, which uniquely identifies a person.

This key is present in all four files.

You are guaranteed that the same SSN value is present in every file, and that it only appears once per file.

In addition, the files are all sorted by SSN, i.e. the SSN values appear in the same order in each file.


#### **Goal 1**
- Your first task is to create iterators for each of the four files that contained cleaned up data, of the correct type (e.g. string, int, date, etc), and represented by a named tuple. For now these four iterators are just separate, independent iterators.

#### **Goal 2**
- Create a single iterable that combines all the columns from all the iterators.
- The iterable should yield named tuples containing all the columns. Make sure that the SSN's across the files match!
- All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file.
- Make sure the SSN is not repeated 4 times - one time per row is enough!


#### **Goal 3**
- Next, you want to identify any stale records, where stale simply means the record has not been updated since 3/1/2017 (e.g. last update date < 3/1/2017). Create an iterator that only contains current records (i.e. not stale) based on the last_updated field from the status_update file.

#### **Goal 4**
- Find the largest group of car makes for each gender.
- Possibly more than one such group per gender exists (equal sizes).

#### **Hint**
- You will not be able to use a simple split approach here
- Instead you should use the csv module and the reader function
- Here's a simple example of how to use it - you will need to expand on this for your project goals, but this is a good starting point


![](/ "")

## **Function created based on Assignment** 

### **read_file** :
- Reads the csv file with ',' delimiter

### **personal_info_generator** :
- Generator for personal_info named tuple , Generates a named tuple for each row in the file

### **fetch_records** :
- provides the list of generator records 

### **vehicle_generator** :
- Generator for vehicle named tuple , Generates a named tuple for each row in the file

### **employment_generator** :
- Generator for employment named tuple , Generates a named tuple for each row in the file

### **update_status_generator** :
-  Generator for update_status named tuple , Generates a named tuple for each row in the file

### **merge_tuples** :
- Merges the records from all the generators into a single list of named tuples ,creates new named tuple by merging other named tuples with key "SSN"

### **combined_generator** :
- Generator for combined named tuple , Generates a named tuple for each row in the file combines all named tuple merged records 

### **vehicle_make_gender_information** :
- Generator for Vehicle Make , Gender from given records

### **vehicle_make_gender_generator** :
- Generator for  Vehicle Make , Gender combinations 

### **show_top_count** :
- Prints Vehicle Make, gender combination count in tabular format

## *Final results* 

### For Females :  Ford , Chevrolet are famous with 48 count
### For Males :  Ford  are famous with 44 count