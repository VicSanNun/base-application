import { useHello } from "../hooks/useHello";
import { Card } from "../components/common/Card";

export const Home = () => {
  const { message, loading } = useHello();

  return (
    <Card title="Home">
      {loading ? (
        <p>Loading...</p>
      ) : (
        <p className="text-lg font-semibold text-blue-600">{message}</p>
      )}
    </Card>
  );
};
