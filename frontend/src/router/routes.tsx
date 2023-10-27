import React, { FC } from "react";
import { Route, Routes } from "react-router-dom";

type DashboardLayout = any;

interface RouteType {
  path: string;
  layout?: FC<DashboardLayout>;
  element: React.LazyExoticComponent<FC>;
}

const routes: RouteType[] = [
  {
    path: "/",
    element: React.lazy(() => import("@/pages/common/main")),
  },
  {
    path: "/character",
    element: React.lazy(() => import("@/pages/common/character")),
  },
  {
    path: "/children/main",
    element: React.lazy(() => import("@/pages/children/main")),
  },
  {
    path: "/children/login",
    element: React.lazy(() => import("@/pages/children/login")),
  },
  {
    path: "/children/profile",
    element: React.lazy(() => import("@/pages/children/profile")),
  },
  {
    path: "/children/character",
    element: React.lazy(() => import("@/pages/children/character")),
  },
  {
    path: "/children/fairytale",
    element: React.lazy(() => import("@/pages/children/fairytale")),
  },
  {
    path: "/parent/login",
    element: React.lazy(() => import("@/pages/parent/login")),
  },
  {
    path: "/parent/main",
    element: React.lazy(() => import("@/pages/parent/main")),
  },
  {
    path: "/parent/profile",
    element: React.lazy(() => import("@/pages/parent/profile")),
  },
  // {
  //   path: "/",
  //   element: () => <Navigate replace to="/main" />,
  // },
  // {
  //   path: "/*",
  //   element: React.lazy(() => import("@/pages/404")),
  // },
];

const RenderRoutes = () => {
  return (
    <React.Suspense fallback={<div>loading...</div>}>
      <Routes>
        {routes.map((route, i) => {
          const RouteElement = route.element;
          const RouteLayout = route.layout || React.Fragment;
          //   const Guard = route.guard || React.Fragment;

          return (
            <Route
              key={i}
              path={route.path}
              element={
                <RouteLayout>
                  <RouteElement />
                </RouteLayout>
              }
            />
          );
        })}
      </Routes>
    </React.Suspense>
  );
};

export default RenderRoutes;
