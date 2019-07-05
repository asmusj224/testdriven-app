import React, { useState, useEffect } from 'react';
import axios from 'axios';
import UserList from '../components/UserList';
import config from 'next/config';

const {
  publicRuntimeConfig: { REACT_APP_USERS_SERVICE_URL }
} = config() || {
  publicRuntimeConfig: { REACT_APP_USERS_SERVICE_URL: 'http://localhost:5001' }
};

export default () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const {
        data: {
          data: { users }
        }
      } = (await axios.get(`${REACT_APP_USERS_SERVICE_URL}/users`)) || {
        data: { data: { users: [] } }
      };

      setUsers(users);
    }
    fetchData();
  }, []);

  return <UserList users={users} />;
};
