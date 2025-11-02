import { useEffect, useState } from "react";
import { apiClient } from "../api/apiClient";

export function useHello() {
  const [message, setMessage] = useState<string>("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiClient.get("/hello")
      .then((res) => setMessage(res.data.message))
      .catch(() => setMessage("Error connecting to API"))
      .finally(() => setLoading(false));
  }, []);

  return { message, loading };
}
