Time Travel Debugger API

Overview
Time Travel Debugger is a backend system designed to simulate how engineers analyze system failures in real-world applications. Instead of simply storing logs, this system reconstructs the sequence of events surrounding a failure, allowing developers to understand what happened before and after an issue occurred.

This project demonstrates backend engineering concepts such as event tracking, timeline reconstruction, and debugging workflows commonly used in production systems.

Key Idea
When a system fails, the most important question is not just what failed, but what led to the failure. This API answers that by rebuilding the timeline of events around any given error.

Features
Store system events with type, message, and timestamp
Retrieve all events in chronological order
Reconstruct event timelines around a specific event
Analyze system behavior leading up to failures
Simulate real-world debugging scenarios

Tech Stack
Python
Flask
SQLite
SQLAlchemy
REST API
Render for deployment

Live Application
https://time-travel-debugger-api.onrender.com

API Endpoints

Home
GET /
Returns confirmation that the API is running

Add Event
POST /events
Stores a new event in the system

Request Body
event_type: Type of event such as INFO or ERROR
message: Description of the event

Get All Events
GET /events
Returns all events sorted by timestamp

Time Travel Debugging
GET /timeline/{event_id}
Returns the selected event along with surrounding events to analyze what happened before and after

Example Use Case

A system encounters a database failure. Instead of guessing the cause, engineers can query the timeline endpoint to see the sequence of events leading up to the failure.

Example flow

Server started
Connection retry attempted
Database failure occurred

This allows engineers to identify patterns and understand the root cause more effectively.

Why This Project Stands Out

This is not a basic CRUD application. It introduces a system-level perspective by focusing on debugging workflows and event analysis. The project reflects how real backend systems are designed to monitor, trace, and diagnose issues in production environments.

It demonstrates

Backend API design
Database integration
System thinking and debugging logic
Real-world problem solving

What I Learned

How to design APIs beyond basic CRUD operations
How to structure backend systems for real-world use cases
How debugging systems work in production environments
How to deploy and manage backend services in the cloud

Future Improvements

Add severity levels such as WARNING and CRITICAL
Implement filtering and search capabilities
Introduce real-time log ingestion
Build a frontend dashboard for visualization
Migrate to scalable databases such as PostgreSQL

Conclusion

This project represents a shift from simple application development to system-oriented thinking. It focuses on solving a real engineering problem and demonstrates the ability to design, build, and deploy meaningful backend systems.
