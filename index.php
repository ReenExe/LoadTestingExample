<?php

require 'vendor/autoload.php';

$app = new \Slim\Slim();

$app->response()->headers->set('Content-Type', 'application/json');

$collection = require_once 'database/collection.php';
$element = require_once 'database/element.php';

class Api
{
    public static function pretty($value)
    {
        echo json_encode($value, JSON_PRETTY_PRINT);
    }
}

$app->get('/', function () use($collection) {
    Api::pretty([
        'success' => true
    ]);
});

$app->get('/api/collections', function () use($collection) {
    Api::pretty($collection);
});

$app->get('/api/collection/:id', function($id) use($app, $collection) {
    if (isset($collection[$id])) {
        return Api::pretty([
            $collection[$id]
        ]);
    }

    $app->response->status(404);
});

$app->get('/api/collection/:id/elements', function($id) use($app, $element) {
    if (isset($element[$id])) {
        return Api::pretty([
            $element[$id]
        ]);
    }

    $app->response->status(404);
});

$app->get('/api/collection/:collectionId/element/:elementId', function($collectionId, $elementId) use($app, $element) {
    if (isset($element[$collectionId][$elementId])) {
        return Api::pretty([
            $element[$collectionId][$elementId]
        ]);
    }

    $app->response->status(404);
});

$app->run();

// sudo php -S 0.0.0.0:80