---
title: OAuth Device Code Grant Flow
---

## OAuth Device Code Grant Flow

The OAuth Device Code Flow is an authorization flow for devices with limited input or display capabilities, like smart TVs, IoT devices, and media consoles. 

In these cases, users can't easily enter login credentials or use a full web browser on the device itself. The Device Code Flow enables users to authorize these devices using a separate device (like a smartphone or computer) to complete the authentication.

Here’s a step-by-step outline of the OAuth Device Code Flow:

### 1. Device Requests Authorization
   - The device (e.g., smart TV) initiates the authorization by sending a request to the OAuth authorization server.
   - This request includes parameters like the *client ID* and *scope*.

### 2. Authorization Server Responds with Device Code and User Code
   - The server responds with a *device code*, a *user code*, a *verification URL*, and a recommended polling interval.
   - The device code is unique to the authorization request.
   - The user code is usually short and can be displayed to the user.

### 3. User Enters User Code on Secondary Device
   - The device displays instructions to the user, typically including:
     - The URL to visit (e.g., https://example.com/device).
     - The User Code they need to enter on this URL.
   - The user goes to the verification URL on a device with a browser (smartphone or computer) and enters the user code to authenticate.

### 4. User Completes Authentication
   - On the secondary device (smartphone or computer), the user logs in and authorizes access to their account.

### 5. Device Polls the Authorization Server
   - Meanwhile, the original device polls the authorization server at the recommended interval, asking if the user has completed the authentication process.
   - If the user hasn’t authenticated yet, the server responds with a “pending” status.

### 6. Device Receives Access Token
   - Once the user has completed authentication, the next poll request from the device receives an *access token*, allowing it to access the user’s data.
   - If the user denies access or doesn’t complete the process in time, the server responds with an error.

### Advantages
   - **User-Friendly on Limited-Input Devices:** Since it avoids entering passwords on the device, it’s easy to use on devices with limited input.
   - **Secure:** Credentials are only entered on a trusted device, reducing the risk of exposure.

### Common Uses
   - Smart TVs and media consoles.
   - IoT devices where logging in directly is inconvenient.

Overall, the Device Code Flow is effective for authenticating devices that are “headless” or lack full input capabilities, allowing users to grant authorization through a separate, more secure device.
