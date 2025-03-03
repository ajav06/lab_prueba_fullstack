import type { Card, ResponseAPI, Set } from '@/models/index';
import { transformObjectToCamelCase } from '@/helpers';
import httpClient from './httpClient';

export const getSets = async (): Promise<ResponseAPI<Set[]>> => {
  const response = await httpClient.get('/sets');
  return transformObjectToCamelCase(response.data);
};

export const getSet = async (id: string): Promise<ResponseAPI<Set>> => {
  const response = await httpClient.get(`/sets/${id}`);
  return transformObjectToCamelCase(response.data);
};

export const getCardsBySet = async (id: string): Promise<ResponseAPI<Card[]>> => {
  const response = await httpClient.get(`/sets/${id}/cards`);
  return transformObjectToCamelCase(response.data);
};
