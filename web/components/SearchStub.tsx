import React from 'react';

export default function SearchStub() {
  return (
    <section>
      <input type="text" placeholder="Search by title, author, DOI..." style={{ padding: '0.5rem', width: '60%' }} />
      <button style={{ marginLeft: '0.5rem', padding: '0.5rem 1rem' }}>Search</button>
      <div style={{ marginTop: '1rem', color: '#666' }}>Search results will appear here.</div>
    </section>
  );
}
