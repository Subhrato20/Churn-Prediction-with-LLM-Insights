import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage('Error fetching message'));
  }, []);

  return (
    <div className="App">
      <h1>FastAPI + React Hello World</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
