import React from 'react';
import Head from 'next/head';
import SearchStub from '../components/SearchStub';

export default function Home() {
  return (
    <>
      <Head>
        <title>ResearchMate — Research Aide</title>
      </Head>
      <main style={{ padding: '2rem', fontFamily: 'system-ui, sans-serif' }}>
        <h1>ResearchMate</h1>
        <p>Fast AI-powered literature discovery — demo scaffold.</p>
        <SearchStub />
      </main>
    </>
  );
}
