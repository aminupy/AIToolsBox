import axios from "axios";

const axiosInstance = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || "http://iam.localhost/",
  headers: {
    "Content-Type": "application/json",
  },
});

export default axiosInstance;
