import React, { useState } from 'react';
import axios from 'axios';

axios.defaults.withCredentials = true;

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [task, setTask] = useState('');
  const [todos, setTodos] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const register = async () => {
    try {
      await axios.post('http://localhost:5000/register', { username, password });
      setPassword('');
      loadTodos();
      setIsLoggedIn(true);
    } catch (error) {
      if (error.response) {
        alert(error.response.data.message);
      } else if (error.request) {
        console.log(error.request);
      } else {
        console.log('Error', error.message);
      }
    }
  };

  const login = async () => {
    const response = await axios.post('http://localhost:5000/login', { username, password });
    if (response.data.message === 'Login successful') {
      loadTodos();
      setIsLoggedIn(true);
      setPassword('');
    } else {
      alert(response.data.message);
    }
  };

  const addTodo = async () => {
    await axios.post(`http://localhost:5000/${username}/todos`, { task });
    setTask('');
    loadTodos();
  };

  const loadTodos = async () => {
    const response = await axios.get(`http://localhost:5000/${username}/todos`);
    setTodos(response.data.todos);
  };

  const deleteTodo = async (todo) => {
    await axios.delete(`http://localhost:5000/todos/${todo.id}`);
    loadTodos();
  };

  const logout = async () => {
    await axios.post('http://localhost:5000/logout');
    setTodos([]);
    setIsLoggedIn(false);
  };

  return (
    <div className="App">
      <h1>Todo App</h1>
      {isLoggedIn ? (
        <>
          <h2>Welcome, {username}!</h2>
          <input placeholder="New todo" value={task} onChange={e => setTask(e.target.value)} />
          <button onClick={addTodo}>Add todo</button>
          <button onClick={logout}>Logout</button>
          <ul>
            {todos.map((todo) => (
              <li key={todo.id}>
                {todo.task}
                <button onClick={() => deleteTodo(todo)}>Delete</button>
              </li>
            ))}
          </ul>
        </>
      ) : (
        <>
          <input placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
          <input placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} />
          <button onClick={register}>Register</button>
          <button onClick={login}>Login</button>
        </>
      )}
    </div>
  );
}

export default App;
