import { NgModule } from "@angular/core";
import { TreeComponent } from "./tree/tree.component";
import { DisplayComponent } from "./tree/display/display.component";
import { InputComponent } from "./tree/input/input.component";
import { ButtonModule } from "primeng/button";
import { InputNumberModule } from "primeng/inputnumber";
import { TooltipModule } from "primeng/tooltip";
import { ReactiveFormsModule } from "@angular/forms";
import { CommonModule } from "@angular/common";
import { SummaryComponent } from "./tree/summary/summary.component";
import { TabViewModule } from "primeng/tabview";
import { BrowserModule } from "@angular/platform-browser";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { OrganizationChartModule } from "primeng/organizationchart";
import { AppComponent } from "./app.component";
import { HeaderComponent } from "./header/header.component";
import { ToStringPipe } from "../pipes/string";

const components = [
    TreeComponent, 
    SummaryComponent, 
    InputComponent, 
    DisplayComponent,
    HeaderComponent,
    AppComponent
];

const pipes = [
    ToStringPipe
];

const modules = [
    CommonModule, 
    BrowserModule, 
    BrowserAnimationsModule, 
    ReactiveFormsModule, 
    ButtonModule, 
    InputNumberModule, 
    TabViewModule, 
    TooltipModule, 
    OrganizationChartModule
];

@NgModule({
    declarations: [
        ...components,
        ...pipes
    ],
    imports: [
        ...modules
    ],
    exports: [
        ...components,
        ...pipes
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {}