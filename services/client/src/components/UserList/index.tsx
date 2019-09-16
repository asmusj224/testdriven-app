import React from 'react';

interface Props {
  users: User[];
}

interface User {
  id: string;
  active: boolean;
  email: string;
}

export default ({ users }: Props) => (
  <div>
    {users.map((user: User) => {
      return <h4 key={user.id}>{user.email}</h4>;
    })}
  </div>
);
