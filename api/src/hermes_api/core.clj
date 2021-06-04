(ns hermes-api.core
  (:gen-class)
  (:require [hermes-api.components :as components]))

(defn run-dev
  [& _]
  (println "\nCreating a [DEV] server...")
  (components/create-and-start-system! :local-system))

(defn -main
  [& _]
  (println "\nCreating the server...")
  (components/create-and-start-system! :base-system))
