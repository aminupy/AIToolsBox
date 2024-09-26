import { create } from "zustand";

type UserState = {
  email: string;
  firstName: string;
  lastName: string;
  userId: string;
};

type Action = {
  setEmail: (email: string) => void;
  setFirstName: (firstName: string) => void;
  setLastName: (lastName: string) => void;
  setUserId: (userId: string) => void;
};

const useUserStore = create<UserState & Action>((set, get) => ({
  email: "",
  firstName: "",
  lastName: "",
  userId: "",
  setEmail: (email) => set({ email }),
  setFirstName: (firstName) => set({ firstName }),
  setLastName: (lastName) => set({ lastName }),
  setUserId: (userId) => set({ userId }),
}));

export default useUserStore;
