import { createStore } from "redux";

import rootReducer from "./Redux/Reducers/allReducers";


export  const Store = createStore(rootReducer);