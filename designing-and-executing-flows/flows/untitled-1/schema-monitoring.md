---
description: Schema Monitoring
---

# Schema Monitoring

Schema monitoring feature provides a robust solution for tracking and managing schema changes in your database environment. This feature is designed to capture the schema of one or more specified tables at a given point in time and continuously compare this snapshot with the current schema. Key functionalities include:

* **Snapshot Capturing**: The feature takes a snapshot of the specified table(s) schema at a user-defined point in time. This snapshot serves as a reference for future comparisons.
* **Continuous Monitoring**: It actively monitors the schema of the targeted table(s) and detects any alterations made after the initial snapshot. This includes changes in table structure, such as added or dropped columns, modified data types, changes in constraints, and more.
* **Change Detection and Notification**: Upon detecting any schema changes, the system promptly notifies users. The notification details the specific alterations, providing a clear and concise overview of how the current schema differs from the original snapshot.
* **Error Reporting**: In the event of unauthorized or unintended schema modifications, the feature flags these as errors. This immediate reporting allows for quick response and rectification, ensuring data integrity and consistency.
* **Use Case Adaptability**: Ideal for environments where schema stability is crucial, such as in production databases or where regulatory compliance requires strict schema control.

This feature enhances the ability to maintain database integrity, comply with regulatory standards, and manage changes efficiently, making it an essential tool for database administrators and teams managing critical data assets.
