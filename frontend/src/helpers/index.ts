/**
 * The `toCamelCase` function converts a string from snake_case to camelCase.
 * @param {string} str - The `str` parameter in the `toCamelCase` function is a string that you want to
 * convert to camel case.
 * @returns The `toCamelCase` function is returning a string where any underscore followed by a
 * lowercase letter is replaced with the uppercase version of that letter.
 */
export const toCamelCase = (str: string): string => {
  return str.replace(/_([a-z])/g, (_, letter) => letter.toUpperCase());
};

/**
 * The function `transformObjectToCamelCase` recursively converts keys of an object (or objects in an
 * array) to camelCase format.
 * @param {T} obj - The `obj` parameter in the `transformObjectToCamelCase` function is the object that
 * you want to transform into camel case. This function recursively converts all keys of the object to
 * camel case format. If the input object is an array, it will map over each item in the array and
 * @returns The `transformObjectToCamelCase` function returns the input object `obj` transformed into
 * camelCase format. If the input is an array, it recursively transforms each item in the array. If the
 * input is an object, it converts the keys of the object to camelCase and recursively transforms
 * nested objects. If the input is neither an array nor an object, it returns the input as is.
 */
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

/* The `export const typesColors` declaration is creating an object named `typesColors` that maps
Pokemon types to their corresponding colors in CSS classes. Each key in the object represents a
Pokemon type (e.g., NORMAL, FIGHTING) and the associated value is the CSS class that provides the
background color for that type. */
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

/**
 * The function `getTypeColor` takes a type as input and returns the corresponding color from a
 * predefined object or a default gray color if no match is found.
 * @param {string} type - The `getTypeColor` function takes a `type` parameter, which is a string
 * representing the type of color we want to retrieve from the pokemon.
 * @returns The function `getTypeColor` returns the color associated with the pokemon `type` from the
 * `typesColors` object. If there is no color associated with the input `type`, it returns the default
 * color `'bg-gray-500'`.
 */
export const getTypeColor = (type: string) => {
  const color = typesColors[type.toUpperCase()] || 'bg-gray-500';
  return color;
};
