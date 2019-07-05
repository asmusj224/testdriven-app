import React from 'react';

interface Props {
  users: User[];
}

interface User {
  id: string;
  username: string;
  active: boolean;
  email: string;
}

export default ({ users }: Props) => (
  <div>
    {users.map((user: User) => {
      return <h4 key={user.id}>{user.username}</h4>;
    })}
  </div>
);
