import { Link } from "react-router-dom";

export const Header = () => (
  <header className="bg-blue-700 text-white py-4 shadow">
    <nav className="container mx-auto flex justify-between">
      <h1 className="text-xl font-bold">React Clean Base</h1>
      <div className="space-x-4">
        <Link to="/" className="hover:underline">Home</Link>
        <Link to="/about" className="hover:underline">About</Link>
      </div>
    </nav>
  </header>
);
