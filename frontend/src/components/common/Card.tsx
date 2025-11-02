import type { ReactNode } from "react";

interface CardProps {
  title: string;
  children: ReactNode;
}

export const Card = ({ title, children }: CardProps) => (
  <div className="bg-white rounded-2xl shadow p-6 max-w-xl mx-auto">
    <h2 className="text-xl font-semibold mb-4">{title}</h2>
    {children}
  </div>
);
  