"use client";
import { useState } from "react";
import axios from "axios";
import { title } from "process";

const HomePage = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
 

  const handleSearch = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/search", {
        params: { q: query },
      });
      setResults(response.data);
    } catch (error) {
      console.error("Error fetching products:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-8 text-black">Product Search</h1>
      <div className="w-full max-w-md">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search for products..."
          className="w-full p-4 mb-4 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
          // Added `text-black` class
        />
        <button
          onClick={handleSearch}
          className="w-full bg-blue-500 text-white py-3 rounded-lg shadow-md hover:bg-blue-600 transition duration-300"
        >
          Search
        </button>
      </div>

      <div className="mt-8 w-full max-w-md">
        {results.length > 0 ? (
          <ul className="space-y-4">
            {results.map((product) => (
              <li
                key={product.id}
                className="p-4 bg-white rounded-lg shadow-md"
              >
                <h3 className="text-xl font-semibold">{product.title}</h3>
                <p className="text-gray-700">{product.description}</p>
                <p className="text-gray-900 font-bold">
                  Price: ${product.price}
                </p>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-600">No products found.</p>
        )}
      </div>
    </div>
  );
};

export default HomePage;
