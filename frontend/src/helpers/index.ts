export const toCamelCase = (str: string): string => {
  return str.replace(/_([a-z])/g, (_, letter) => letter.toUpperCase());
};

export const transformObjectToCamelCase = <T>(obj: T): T => {
  if (Array.isArray(obj)) {
    return obj.map((item) => transformObjectToCamelCase(item)) as unknown as T;
  }
  if (obj !== null && typeof obj === 'object') {
    const newObj: Record<string, any> = {};
    for (const key in obj as Record<string, any>) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        const camelCaseKey = toCamelCase(key);
        newObj[camelCaseKey] = transformObjectToCamelCase((obj as Record<string, any>)[key]);
      }
    }
    return newObj as T;
  }
  return obj;
};

export const typesColors: Record<string, string> = {
  NORMAL: 'bg-gray-500',
  FIGHTING: 'bg-yellow-500',
  FLYING: 'bg-blue-500',
  POISON: 'bg-purple-500',
  GROUND: 'bg-yellow-500',
  ROCK: 'bg-gray-500',
  BUG: 'bg-green-500',
  GHOST: 'bg-indigo-500',
  STEEL: 'bg-gray-500',
  FIRE: 'bg-red-500',
  WATER: 'bg-blue-500',
  GRASS: 'bg-green-500',
  ELECTRIC: 'bg-yellow-500',
  PSYCHIC: 'bg-pink-500',
  ICE: 'bg-blue-500',
  DRAGON: 'bg-purple-500',
  DARK: 'bg-gray-500',
  FAIRY: 'bg-pink-500',
  UNKNOWN: 'bg-gray-500',
  SHADOW: 'bg-gray-500',
};

export const getTypeColor = (type: string) => {
  const color = typesColors[type.toUpperCase()] || 'bg-gray-500';
  return color;
};
