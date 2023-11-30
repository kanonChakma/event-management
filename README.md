# Event Management

## Overview

The Event Management API allows users to view and interact with events, register for events, and retrieve information about registered events.

## Endpoints

### 1. Get a List of Events

#### Endpoint:

- **URL:** `/api/events/`
- **Method:** GET
- **Description:** Retrieve a list of all available events.
- **Response:**
  - Status Code: 200 (OK)

### 2. Get Event Details

#### Endpoint:

- **URL:** `/api/event/<int:event_id>/`
- **Method:** GET
- **Description:** Retrieve details for a specific event.
- **Parameters:**
  - `event_id` (int): ID of the event.
- **Response:**
  - Status Code: 200 (OK)
  - Status Code: 404 (Not Found) if the event with the given ID does not exist.

### 3. Register for an Event

#### Endpoint:

- **URL:** `/api/event/register/<int:event_id>/`
- **Method:** POST
- **Description:** Register the authenticated user for a specific event.
- **Parameters:**
  - `event_id` (int): ID of the event.
- **Response:**
  - Status Code: 201 (Created) if registration is successful.
  - Status Code: 400 (Bad Request) if the user is already registered for the event.
  - Status Code: 404 (Not Found) if the event with the given ID does not exist.

### 4. Get Registered Events for a User

#### Endpoint:

- **URL:** `/api/registered-events/`
- **Method:** GET
- **Description:** Retrieve a list of events that the authenticated user has registered for.
- **Response:**
  - Status Code: 200 (OK)
