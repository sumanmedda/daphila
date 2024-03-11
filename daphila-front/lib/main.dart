import 'package:daphila/view/dashboard.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    var home = const Dashboard();
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Daphilo',
      theme: ThemeData(
        brightness: Brightness.dark,
        primarySwatch: Colors.blue,
      ),
      home: home,
    );
  }
}
