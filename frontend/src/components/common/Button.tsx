interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    label: string;
  }
  
  export const Button = ({ label, ...props }: ButtonProps) => (
    <button
      className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md shadow"
      {...props}
    >
      {label}
    </button>
  );
  