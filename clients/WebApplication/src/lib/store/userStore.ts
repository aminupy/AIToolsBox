import { create } from "zustand";

type UserState = {
  email: string;
  firstName: string;
  lastName: string;
};

type Action = {
  setEmail: (email: string) => void;
  setFirstName: (firstName: string) => void;
  setLastName: (lastName: string) => void;
};

const useUserStore = create<UserState & Action>((set) => ({
  email: "",
  firstName: "",
  lastName: "",
  setEmail: (email) => set({ email }),
  setFirstName: (firstName) => set({ firstName }),
  setLastName: (lastName) => set({ lastName }),
}));

export default useUserStore;
