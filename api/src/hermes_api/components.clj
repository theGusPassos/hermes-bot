(ns hermes-api.components
  (:require [com.stuartsierra.component :as component]
            [hermes-api.components.dummy-config :as config]
            [hermes-api.components.service :as service]
            [hermes-api.components.servlet :as servlet]
            [hermes-api.components.routes :as routes]
            [hermes-api.components.system-utils :as system-utils]
            [hermes-api.service :as service-impl]))

(def base-config-map {:environment  :prod
                      :port         8080})

(def local-config-map {:environment :dev-port
                       :port        8080})

(defn base []
  (component/system-map
   :config (config/new-config base-config-map)
   :routes (routes/new-routes #'service-impl/routes)
   :service (component/using (service/new-service) [:config :routes])
   :servlet (component/using (servlet/new-servlet) [:service])))

(defn local []
;  (s/set-fn-validation! true)
  (merge (base)
         (component/system-map
          :config (config/new-config local-config-map))))

(def systems-map
  {:base-system base
   :local-system local})

(defn create-and-start-system!
  ([] (create-and-start-system! :base-system))
  ([env]
   (system-utils/bootstrap! ((env systems-map)))))

(defn ensure-system-up! [env]
  (or (deref system-utils/system)
      (create-and-start-system! env)))

(defn stop-system! [] (system-utils/stop-components!))