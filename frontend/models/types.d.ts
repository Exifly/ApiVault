export interface CategoryObject {
  name: string;
  icon: string | string[];
}

export interface CategoriesDict {
  [key: string]: string | string[];
}

export interface TrendingCategory {
  api_count: number,
  name: string;
}

export interface APIType {
  id: number;
  name: string;
  auth: string;
  category: string;
  cors: boolean;
  description: string;
  https: boolean;
  url: string;
}

export interface GithubContributor {
  id: number;
  login: string;
  avatar_url: string;
  html_url: string;
}

export interface FirebaseConfig {
  apiKey: string;
  authDomain: string;
  projectId: string;
  storageBucket: string;
  messagingSenderId: string;
  appId: string;
  measurementId: string;
}

export interface OAuthToken {
  refresh: string;
  access: string;
}

export interface GoogleOAauth2Config {
  username: string;
  email: string;
  tokens: OAuthToken;
}

/* Global */
declare global {
  /* Abstractions */
  interface Window {
    handleCredentialResponse: () => void;
  }
}