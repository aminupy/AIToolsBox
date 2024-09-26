import axios from "axios";

const axiosInstance = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || "http://iam.localhost/",
  headers: {
    "Content-Type": "application/json",
  },
});

// Add a response interceptor to handle errors globally
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    let userFriendlyMessage = "An unknown error occurred. Please try again.";

    if (error.response) {
      // Handle specific status codes and provide user-friendly messages
      switch (error.response.status) {
        case 400:
          userFriendlyMessage =
            "The provided code is invalid. Please try again.";
          break;
        case 401:
          userFriendlyMessage =
            "You are not authorized to perform this action.";
          break;
        case 404:
          userFriendlyMessage = "The requested resource was not found.";
          break;
        case 500:
          userFriendlyMessage =
            "Internal server error. Please try again later.";
          break;
        default:
          userFriendlyMessage = "Something went wrong. Please try again.";
      }
    } else if (error.request) {
      userFriendlyMessage =
        "No response from the server. Please check your connection.";
    }

    console.log("Error response", error.response?.data); // For debugging purposes

    return Promise.reject(userFriendlyMessage); // Reject the promise with a user-friendly message
  }
);

export default axiosInstance;
