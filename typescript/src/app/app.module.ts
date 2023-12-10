import { NgModule } from "@angular/core";
import { TreeComponent } from "./tree/tree.component";
import { DisplayComponent } from "./tree/display/display.component";
import { InputComponent } from "./tree/input/input.component";
import { ButtonModule } from "primeng/button";
import { InputNumberModule } from "primeng/inputnumber";
import { TooltipModule } from "primeng/tooltip";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { CommonModule } from "@angular/common";
import { TabViewModule } from "primeng/tabview";
import { BrowserModule } from "@angular/platform-browser";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { OrganizationChartModule } from "primeng/organizationchart";
import { AppComponent } from "./app.component";
import { HeaderComponent } from "./header/header.component";
import { ToStringPipe } from "../pipes/string";
import { MenubarModule } from 'primeng/menubar';
import { SearchComponent } from "./tree/display/search/search.component";
import { InputTextModule } from "primeng/inputtext";

const components = [
    TreeComponent, 
    InputComponent, 
    DisplayComponent,
    HeaderComponent,
    AppComponent,
    SearchComponent
];

const pipes = [
    ToStringPipe
];

const modules = [
    CommonModule, 
    BrowserModule, 
    BrowserAnimationsModule, 
    FormsModule,
    ReactiveFormsModule, 
    ButtonModule, 
    InputNumberModule, 
    TabViewModule, 
    TooltipModule, 
    OrganizationChartModule,
    InputTextModule,
    MenubarModule
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
        ...pipes,
        ...modules
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {}