# Roles and Permissions

## Roles and Permissions on Vexdata.io

### Summary

The hierarchical structure of roles and permissions on Vexdata.io ensures a clear and organized approach to user management and project control. Each level, from Admin to User, has defined responsibilities and permissions to maintain a balanced and secure environment for data validation and testing.

This documentation aims to provide a comprehensive understanding of the roles and permissions, helping users navigate their responsibilities and capabilities within Vexdata.io effectively.

### Admin

* **Role Overview**: The Super Admin holds the highest level of authority within the Vexdata.io platform.
* **Permissions**:
  * **Enable/Disable Features**: Ability to activate or deactivate features for all users.
    * Set Global Default Time Zone
    * Update Software
    * Enable/Disable Features for all users.
  * **User Management**: Can assign/revoke any permission to any user or make any user as an admin.
  * **Access to Reports**: Full access to all administrative reports and analytics. These reports are restricted to only Admin.



{% hint style="info" %}
Admin can be set only on the server properties file.&#x20;
{% endhint %}

### Project Owner

* **Role Overview**: The Project Owner is the user who creates a project and holds significant control over that project's settings and user access. There can be one or more owners for a project.  An owner can add/remove other owners.&#x20;
  *   When a new project is created, no other user can access that project. To add acces, do that following.


* **Permissions**:
  * **User Access Management**: Can grant access to other users, allowing them to read, write, execute, and delete test cases within the project.
  * **Ownership Transfer**: Ability to assign other users as project owners, sharing the ownership and control over the project.



{% embed url="https://www.loom.com/share/a54231af26ae49abbdccc4a2f44999b9?sid=6059570a-5621-4174-b570-85ab0e7aeb77" %}
Steps to Add users/edit permissions for a user
{% endembed %}

### Regular User

* **Role Overview**: Regular Users are individuals who are granted specific permissions within a project by the Project Owner.
* **Permissions**:
  * **Access Levels**: Permissions are based on what the Project Owner grants, which can include reading, writing, executing, and deleting test cases.

