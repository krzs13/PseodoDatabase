# PseudoDatabase

COMMANDS
1. Create document: CREATE DOCUMENT file_name (column1, column2...)
2. Add record: ADD (value1, value2...) TO file_name
3. Display values from columns (* all): SELECT (column1, column2...) FROM file_name
4. Count unique values in selected column: COUNT DISTINCT (column) FROM file_name
5. Delete records with specific value: DELETE FROM file_name WHERE column=value
6. Export files to zip package: EXPORT FROM file_name1, file_name2...
7. Import files from zip package: IMPORT FROM zip_package_name
8. Display document in JSON format: JSON file_name

Commands are not case sensitive. 
User need to split values by comma and space ', ' -> PROPER: value1, value2 NOT PROPER: value1,value2.
Commas and spaces are accepted in columns and values -> EXAMPLE: 'na,,,, me'.
