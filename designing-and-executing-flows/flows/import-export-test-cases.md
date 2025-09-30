---
description: >-
  Learn how to import and export test cases in Vexdata, both individually and in
  bulk, to streamline your data validation workflows.
---

# Import/Export Test Cases

### Overview



Vexdata provides flexible import and export capabilities for test cases, allowing you to backup, share, and migrate your data validation configurations. You can export and import test cases either individually or in bulk.



### Export Test Cases



#### Export Individual Test Case



To export a single test case:



1. Navigate to the **Test Cases** page
2. Locate the test case you want to export in the test cases list
3. Click the **three-dot menu** (⋮) icon on the right side of the test case row
4. Select **Export** from the dropdown menu
5. The test case will be downloaded as a JSON file to your computer

#### Export Multiple Test Cases (Bulk Export)



To export multiple test cases at once:



1. Navigate to the **Test Cases** page
2. Select the checkboxes next to the test cases you want to export
3. Click the **More** dropdown button in the top toolbar
4. Select **Export Test Cases** from the dropdown menu
5. All selected test cases will be downloaded as a JSON file

**Alternative Method:**

* To export all test cases without selection, simply click **More** > **Export Test Cases** without selecting any checkboxesThis will export all test cases in your project

### Import Test Cases



#### Import Single Test Case



To import a single test case:



1. Navigate to the **Test Cases** page
2. Click the **More** dropdown button in the top toolbar
3. Select **Import Single Test Case** from the dropdown menu
4. Browse and select the JSON file containing the test case
5. Click **Open** to import
6. The test case will be added to your project

#### Import Multiple Test Cases (Bulk Import)



To import multiple test cases at once:



1. Navigate to the **Test Cases** page
2. Click the **More** dropdown button in the top toolbar
3. Select **Import Bulk TestS** from the dropdown menu
4. Browse and select the JSON file containing multiple test cases
5. Click **Open** to import
6. All test cases from the file will be added to your project

### File Format



Test cases are exported and imported in JSON format. The exported file contains:

* Test case configurationSource and target dataset informationTest type and validation rulesMappings and variablesAll metadata associated with the test case

### Use Cases



**Backup and Recovery**

* Regularly export your test cases to create backupsRestore test cases if needed

**Environment Migration**

* Export test cases from a development environmentImport them into staging or production environments

**Team Collaboration**

* Share test case configurations with team membersImport standardized test cases across projects

**Template Creation**

* Export commonly used test cases as templatesImport and modify them for new projects

### Additional Bulk Operations



When test cases are selected, the **More** menu provides additional bulk operations:

* **Copy Test Cases** - Duplicate selected test cases**Add Test Cases to Batch** - Add multiple test cases to a batch for execution**Delete Test Cases** - Remove selected test cases from the project**Manage Labels** - Apply or modify labels for selected test cases

### Tips and Best Practices



1. **Naming Convention**: Use descriptive names for exported files to easily identify their contents
2. **Version Control**: Include date or version numbers in exported file names
3. **Regular Backups**: Export critical test cases regularly to prevent data loss
4. **Validation After Import**: Review imported test cases to ensure all configurations are correct
5. **File Organization**: Store exported test case files in a structured folder system

### Important Notes



* Exported test cases retain their original Test Case IDsWhen importing, ensure the source and target datasets referenced in the test cases exist in your projectIf datasets don't exist, you may need to update the test case configurations after importBulk operations are more efficient when working with large numbers of test cases
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
